from django.shortcuts import render
import numpy as np
from numpy import linalg
from main.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
import json
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def base_context(request):
    context = dict()
    context["user"] = request.user
    return context


# View for index page
def index(request):
    context = base_context(request)
    context["site_name"] = "Последняя теорема Фарма"  # Строка перед | в title страницы
    context["page_name"] = "Главная"  # Строка после |
    return render(request, "pages/index.html", context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", context={"form": form})

    def post(self, request):
        bound_form = LoginForm(request.POST)

        if bound_form.is_valid():
            login_user = bound_form.cleaned_data["login"]
            password = bound_form.cleaned_data["password"]

            user = authenticate(username=login_user, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect("/")

        return render(request, "login.html", context={"form": bound_form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


class RegistrView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", context={"form": form})

    def post(self, request):
        bound_form = RegisterForm(request.POST)

        if bound_form.is_valid():
            new_user = bound_form.save_user()
            if request.user.is_staff:
                return render(request, "index.html")
            else:
                return HttpResponseRedirect("/")

        return render(request, "register.html", context={"form": bound_form})


@login_required
def profile(request):
    context = base_context(request)
    context["site_name"] = "Личный кабинет"
    results = QuizResult.objects.filter(user=request.user)
    context["results"] = results
    return render(request, "personal.html", context)


def page_not_found(request, exception=None):
    return render(request, "404.html", status=404)


# View for numeric methods page
def numericMehods(request):
    context = base_context(request)
    context["site_name"] = "Численные методы"
    context["page_name"] = "Главная"
    return render(request, "pages/numericMethods.html", context)

@csrf_exempt
def crammer_method(request):
    context = {"site_name": "Численные методы", "page_name": "Метод Краммера"}
    if request.method == "POST":
        n = int(request.POST.get("size",2))
        n_value = range(n)
        context["n"] = n 
        context["n_value"] = n_value
        A = np.zeros((n,n))
        b = np.zeros(n)

        list_array_crammer = request.POST.getlist("fake_matrix")
        list_crammet_vector = request.POST.getlist("fake_matrix_vector")
        if len(list_array_crammer) != 0:
            count = 0
            for i in range(n):
                for j in range(n):
                    A[i][j] = int(list_array_crammer[count])
                    count += 1
                b[i] = int(list_crammet_vector[i])
        
        # Compute determinant of A
            det_A = np.linalg.det(A)

            # Initialize context dictionary
            context = {
                'A': A,
                'b': b,
                'det_A': det_A,
                'x': np.zeros(n).tolist(),
                'step': 0
            }
            
            steps = []
            # Check if determinant is nonzero
            if det_A != 0:
                # Loop over columns of A to solve for each variable
                for i in range(n):
                    # Create copy of A with ith column replaced by b
                    
                    Ai = A.copy()
                    print(Ai)
                    Ai[:, i] = b


                    # Compute determinant of Ai
                    det_Ai = np.linalg.det(Ai)

                    # Compute solution for ith variable
                    xi = det_Ai / det_A
                    steps.append((i + 1, A, b, xi))
                    # Update context dictionary with current step and solution
                    context['x'][i] = xi
                    context['step'] = i+1
                    context['steps'] = steps
                    
            else:
                # If determinant is zero, system is inconsistent
                context['error'] = 'System is inconsistent'    
        
        return JsonResponse(
            {
                "tableHTML": render_to_string("partials/normal_table.html", context),
                "resultsHTML": render_to_string(
                    "partials/results_cramer.html", context
                )
                
            }
        )
    
    return render(request, "pages/crammer.html", context)


@csrf_exempt
def gauss_method(request):
    context = {"site_name": "Численные методы", "page_name": "Метод Гаусса"}

    if request.method == "POST":
        # Code to handle AJAX request

        # Get value of size user input and parse it into context
        n = int(request.POST.get("size", 2))
        n_value = range(n)

        context["n"] = n
        context["s_value"] = n
        context["n_value"] = n_value

        # Get the same value to generate extra table tr's
        iterable_for_template = n + 1

        # For generating table
        context["j_value"] = range(iterable_for_template)

        list_array_gauss = request.POST.getlist("fake_matrix")
        array_gauss = []
        if len(list_array_gauss) != 0:
            size = round(len(list_array_gauss) ** 0.5)
            for с in range(size):
                array_gauss.append([0] * len(list_array_gauss) // 2)
            count = 0
            for i in range(size):
                for j in range(len(list_array_gauss) // 2):
                    array_gauss[i][j] = float(list_array_gauss[count])
                    count += 1

        array_gauss1 = np.asarray(array_gauss)

        if len(array_gauss1) != 0:
            for nrow, row in enumerate(array_gauss1):
                divider = row[nrow]
                row /= divider
                for lower_row in array_gauss1[nrow + 1 :]:
                    factor = lower_row[nrow]
                    lower_row -= factor * row
            for nrow in range(len(array_gauss1) - 1, 0, -1):
                row = array_gauss1[nrow]
                for upper_row in array_gauss1[:nrow]:
                    factor = upper_row[nrow]
                    upper_row[-1] -= factor * row[-1]
                    upper_row[nrow] = 0

            m1 = np.copy(array_gauss1)
            roots = m1[:, -1]
            print(roots)

        # Create a JSON response with the updated table HTML
        return JsonResponse(
            {
                "tableHTML": render_to_string("partials/table.html", context),
            }
        )
    return render(request, "pages/gauss.html", context)


# View for finding determinant of matrix in numerical methods
@csrf_exempt
def determinant(request):
    context = {"site_name": "Численные методы", "page_name": "Определитель матрицы"}

    if request.method == "POST":
        n = int(request.POST.get("size", 2))
        context["n"] = n
        n_value = range(n)
        context["n_value"] = n_value

        listArrayDeterminant = request.POST.getlist("fake_matrix")
        arrayDeterminant = []

        if len(listArrayDeterminant) != 0:
            size = round(len(listArrayDeterminant) ** 0.5)
            for с in range(size):
                arrayDeterminant.append([0] * size)
            count = 0
            for i in range(size):
                for j in range(size):
                    arrayDeterminant[i][j] = int(listArrayDeterminant[count])
                    count += 1

        np.asarray(arrayDeterminant)

        if len(arrayDeterminant) != 0:
            determinant = round(linalg.det(arrayDeterminant), 2)

            context["arrayDeterminant"] = arrayDeterminant
            context["determinant"] = determinant

        # Create a JSON response with the updated determinant and table HTML
        return JsonResponse(
            {
                "tableHTML": render_to_string("partials/simple_table.html", context),
                "resultsHTML": render_to_string(
                    "partials/results_determinant.html", context
                ),
            }
        )

        # Render the partial template for the matrix display

    # Render the initial page
    return render(request, "pages/determinant.html", context)


# View for matrix rules in numeric methods page
def matrixLawOfEquality(request):
    context = {"site_name": "Численные методы", "page_name": "Законы матриц"}

    # Get size of array from user input and get it into context
    if request.method == "POST":
        n = int(request.POST.get("size", 2))
        context["n"] = n
        n_value = range(n)
        context["n_value"] = n_value

    # Get list of user input (first matrix) return listArray = ['2','3','5' etc.]
    listArray = request.POST.getlist("fake_matrix")

    # Get list of user input (second matrix) return listArray = ['2','3','5' etc.]
    listArray2 = request.POST.getlist("fake_matrix_second")

    # Declaring of first array
    fisrtArray = []

    # Declaring of second array
    secondArray = []

    # Filling first array using listArray. (round(len(listArray)**0.5)) is for correct filling. Saying easy it's size of arrays
    if len(listArray) != 0:
        size = round(len(listArray) ** 0.5)
        for с in range(size):
            fisrtArray.append([0] * size)
        count = 0
        for i in range(size):
            for j in range(size):
                fisrtArray[i][j] = int(listArray[count])
                count += 1

    # Filling second array using listArray2
    if len(listArray2) != 0:
        size = round(len(listArray) ** 0.5)
        for g in range(size):
            secondArray.append([0] * size)
        count1 = 0
        for i in range(size):
            for j in range(size):
                secondArray[i][j] = int(listArray2[count1])
                count1 += 1

    # Declaration of third array
    thirdArray = np.ones(2, dtype=np.int64)

    # Converting first and second array to NumPy array
    np.asarray(fisrtArray)
    np.asarray(secondArray)

    if len(fisrtArray) != 0:
        # Getting the value of third matrix using multiplication of first and second matrix
        thirdArray = np.dot(fisrtArray, secondArray)

        # Summ of first and second matrix (A+B)
        sumOfFirstAndSecondMatrix = np.add(fisrtArray, secondArray)

        # Result of left side of rule (A+B)*C
        resultOfLeftSide = np.dot(sumOfFirstAndSecondMatrix, thirdArray)

        # Multiplication of first and third matrix (AC)
        multiplicationOfFirstAndThirdMatrix = np.dot(fisrtArray, thirdArray)

        # Multiplication of second and third matrix (BC)
        multiplicationOfSecondAndThirdMatrix = np.dot(secondArray, thirdArray)

        # Result of right side of rule = AC + BC
        resultOfRightSide = np.add(
            multiplicationOfFirstAndThirdMatrix, multiplicationOfSecondAndThirdMatrix
        )

        # Getting first and second array to context to display on site
        context["firstArray"] = fisrtArray
        context["secondArray"] = secondArray
        context["thirdArray"] = thirdArray
        context["resultOfLeftSide"] = resultOfLeftSide
        context["resultOfRightSide"] = resultOfRightSide
    return render(request, "pages/matrixlaws.html", context)


@login_required
def quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    return render(request, "pages/quiz.html", {"quiz": quiz, "questions": questions,})


@login_required
def submit_quiz(request, quiz_id):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    score = 0
    total = len(questions)
    for question in questions:
        answer_id = request.POST.get("answer_" + str(question.id))
        if answer_id:
            answer = Answer.objects.get(id=int(answer_id))
            if answer.is_correct:
                score += 1
    result = QuizResult.objects.create(
        quiz=quiz, user=request.user, score=score, total=total
    )
    return render(
        request, "pages/results.html", {"quiz": quiz, "score": score, "total": total}
    )


@csrf_exempt
def iterative_method(request):
    context = {"site_name": "Численные методы", "page_name": "Метод итераций"}
    if request.method == "POST":
        n = int(request.POST.get("size",2))
        n_value = range(n)
        context["n"] = n 
        context["n_value"] = n_value
        print(context["n_value"])
        A = np.zeros((n,n))
        b = np.zeros(n)

        list_array_iterative = request.POST.getlist("fake_matrix")
        list_iterative_vector = request.POST.getlist("fake_matrix_vector")
        if len(list_array_iterative) != 0:
            count = 0
            for i in range(n):
                for j in range(n):
                    A[i][j] = int(list_array_iterative[count])
                    count += 1
                b[i] = int(list_iterative_vector[i])

            # Initialize context dictionary
            context = {
                'A': A,
                'b': b,
                'x': np.zeros(n).tolist(),
                'step': 0
            }

            steps = []

            # Check for diagonal dominance
            is_diagonally_dominant = True
            for i in range(n):
                row_sum = np.sum(np.abs(A[i])) - np.abs(A[i][i])
                if np.abs(A[i][i]) <= row_sum:
                    is_diagonally_dominant = False
                    break
                
            if is_diagonally_dominant:
                # Loop over iterations of the iterative method
                x = np.zeros(n)
                for iteration in range(10):
                    # Compute the next approximation using the iterative method
                    x_next = np.zeros(n)
                    for i in range(n):
                        sigma = 0
                        for j in range(n):
                            if j != i:
                                sigma += A[i][j] * x[j]
                        x_next[i] = (b[i] - sigma) / A[i][i]

                    # Compute the error between the current and next approximations
                    error = np.linalg.norm(x_next - x, ord=np.inf)

                    # Append the current step to the list of steps
                    steps.append((iteration + 1, x.tolist(), error))

                    # Update the current approximation with the next approximation
                    x = x_next
                    print(x)
                # Update context dictionary with the final solution and steps
                context['x'] = x.tolist()
                context['step'] = iteration + 1
                context['steps'] = steps

            else:
                context['error'] = 'Matrix A is not diagonally dominant'

        return JsonResponse(
            {
                "tableHTML": render_to_string("partials/normal_table.html", context),
                "resultsHTML": render_to_string(
                    "partials/results_iterative.html", context
                ),
                
            }
        )

    return render(request, "pages/iterative.html", context)


@csrf_exempt
def newton_method(request):
    context = {"site_name": "Численные методы", "page_name": "Метод Ньютона"}
    if request.method == "POST":
        n = int(request.POST.get("size", 2))
        n_value = range(n)
        context["n"] = n
        context["n_value"] = n_value
        A = np.zeros((n, n))
        b = np.zeros(n)

        list_array_newton = request.POST.getlist("fake_matrix")
        list_newton_vector = request.POST.getlist("fake_matrix_vector")
        if len(list_array_newton) != 0:
            count = 0
            for i in range(n):
                for j in range(n):
                    A[i][j] = int(list_array_newton[count])
                    count += 1
                b[i] = int(list_newton_vector[i])

            # Initialize context dictionary
            context = {
                'A': A,
                'b': b,
                'x': np.zeros(n).tolist(),
                'step': 0
            }

            steps = []

            # Loop over iterations of the Newton method
            x = np.zeros(n)
            for iteration in range(10):
                # Evaluate the system of equations and its Jacobian at x
                f = np.dot(A, x) - b
                J = np.zeros((n, n))
                for i in range(n):
                    for j in range(n):
                        J[i, j] = A[i, j]

                # Solve the linear system J * delta_x = -f for delta_x
                delta_x = np.linalg.solve(J, -f)

                # Update the solution x
                x = x + delta_x

                # Append the current step to the list of steps
                steps.append((iteration + 1, x.tolist()))

            # Update context dictionary with the final solution and steps
            context['x'] = x.tolist()
            context['step'] = iteration + 1
            context['steps'] = steps

        return JsonResponse(
            {
                "tableHTML": render_to_string("partials/normal_table.html", context),
                "resultsHTML": render_to_string(
                    "partials/results_newton.html", context
                )
            }
        )

    return render(request, "pages/newton.html", context)