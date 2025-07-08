from .models import CompanyInfo
from datetime import datetime

def company_info(request):
    # Получаем единственную запись с данными компании
    company = CompanyInfo.objects.first()
    return {
        'company': company,
        'current_year': datetime.now().year,
    }
