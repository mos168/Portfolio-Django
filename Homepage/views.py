from django.shortcuts import render,redirect

# Create your views here.
def Homepage(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email_address']
        message = request.POST['message']

        print(fname, lname, email, message)
        return redirect('Homepage')
    else:
        return render(request, 'index.html')
    # return render(request, 'index.html')
