from rest_framework.views import APIView
from rest_framework.response import Response
from companies.models import Company

from .faiss_engine import search
from .gemini_llm import generate_human_reply


class ChatAPIView(APIView):

    def post(self, request):

        company_code = request.data.get("company_code")
        token = request.data.get("api_token")
        message = request.data.get("message")

        if not all([company_code, token, message]):
            return Response({"error": "Missing fields"}, status=400)

        try:
            Company.objects.get(code=company_code, api_token=token)
        except Company.DoesNotExist:
            return Response({"error": "Unauthorized"}, status=401)

        # 🔍 Fetch relevant company data via FAISS
        chunks = search(company_code, message)

        context = "\n".join(chunks)

        # 🤖 Ask Gemini to reply professionally
        reply = generate_human_reply(context, message)

        return Response({"reply": reply})
