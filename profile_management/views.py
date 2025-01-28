from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm
from .models import UserProfile

@login_required
def upload_or_update_profile_picture(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Replace 'profile' with your desired URL name
    else:
        form = ProfilePictureForm(instance=user_profile)

    return render(request, 'profile_picture_form.html', {'form': form, 'profile': user_profile})
