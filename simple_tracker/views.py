from django.shortcuts import render, redirect
from simple_tracker.models import Course
from simple_tracker.forms import DeleteForm, CourseForm

# Create your views here.
def index(request):
    course_list = Course.objects.order_by('misses')
    course_dict = {'courses':course_list}
    return render(request, 'simple_tracker/index.html', context=course_dict)

def register(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(index)
        else:
            print('Form invalid!')
    return render(request, 'simple_tracker/register_class.html', context={'form':form})

def remove(request):
    form = DeleteForm()
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['course_choice']
            c = Course.objects.get(pk = name).delete()
            return redirect(index)
    return render(request, 'simple_tracker/remove_class.html', context={'form':form})

def increase_miss(request):
    if request.method == 'POST':
        name = request.POST.get('add')
        c = Course.objects.get(pk = name)
        c.misses = c.misses + 1
        c.save()
        print(name)
        return redirect(index)
    return redirect(index)


def decrease_miss(request):
    if request.method == 'POST':
        name = request.POST.get('remove')
        c = Course.objects.get(pk = name)
        if c.misses > 0:
            c.misses = c.misses - 1
            c.save()
        print(name)
        return redirect(index)
    return redirect(index)
