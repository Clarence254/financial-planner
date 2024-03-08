from django.shortcuts import render

# Create your views here.

def financial_planner(request):
    if request.method == 'POST':
        income = request.POST.get('income', None)
        if not income:
            message = "Please enter your income."
            return render(request, 'app/financial_planner.html', {'message': message})
        
        income = float(income)
        categories = {
            'Food': {'min': income * 0.10, 'max': income * 0.20},
            'Clothing': {'min': income * 0.03, 'max': income * 0.05},
            'Transportation': {'min': income * 0.15, 'max': income * 0.20},
            'Housing': {'min': income * 0.35, 'max': income * 0.35},
            'Utilities': {'min': income * 0.05, 'max': income * 0.05},
            'Medical': {'min': income * 0.03, 'max': income * 0.03},
            'Debt Payments': {'min': income * 0.05, 'max': income * 0.15},
            'Savings': {'min': income * 0.05, 'max': income * 0.10},
            'Personal & Discretionary': {'min': income * 0.05, 'max': income * 0.10},
        }
        return render(request, 'app/result.html', {'categories': categories})
    return render(request, 'app/financial_planner.html')

