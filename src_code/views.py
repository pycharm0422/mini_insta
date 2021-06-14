from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, AddPosts
from .models import Detail, Post, Message, Room
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def home(request):
    posts = Post.objects.all()
   
    context = {
        'posts':posts,
    }
    return render(request, 'src_code/home.html', context)



def follow_unfollow(request, id_user, value):
    main_user = Detail.objects.get(user=request.user)
    add_following = Detail.objects.get(user__id=id_user)
    
    if value == '1':
        main_user.following.add(add_following.user)
        add_following.followers.add(main_user.user)

    if value == '0':
        main_user.following.remove(add_following.user)
        add_following.followers.remove(main_user.user)

    return redirect('user-page', id_user)


def message(request, receiver):
    sender = request.user
    receiver = User.objects.get(username=receiver)
    name1 = str(str(sender) + str(receiver))
    name2 = str(str(receiver) + str(sender))
    print(name1)
    if Room.objects.filter(room_name=name1).exists():
        room = Room.objects.get(room_name=name1)

    elif Room.objects.filter(room_name=name2).exists():
        room = Room.objects.get(room_name=name2)

    else:
        room = Room.objects.create(room_name=name1)
        # Room.objects.get(room_name=name1).message.add(new_message)

    
    if request.method == 'POST':
        message = request.POST['message']
        new_message = Message.objects.create(message=message, sender=sender, receiver=receiver)
        room.message.add(new_message)


        return redirect('message-page', receiver=receiver)
    try:
        messages = Room.objects.get(room_name=name1).message.all()
    except:
        messages = Room.objects.get(room_name=name2).message.all()

    context = {
        'messages':messages,
        'receiver_obj':receiver,
    }
    return render(request, 'src_code/message.html', context)

    
# def message(request, receiver):
#     sender = request.user
#     receiver = User.objects.get(username=receiver)
#     if request.method == 'POST':
#         message = request.POST['message']
#         new_message = Message.objects.create(message=message, sender=sender, receiver=receiver, connection=[sender.username, receiver.username])
#         Detail.objects.get(user=sender).message.add(new_message)
#         Detail.objects.get(user=receiver).message.add(new_message)
#         new_message.save()

#         return redirect('message-page', receiver=receiver)
    
#     messages = Detail.objects.get(user=request.user)
#     messages = messages.message.filter(sender=sender, receiver=receiver)
#     # one_to_one_message = messages.message.filter()
    
#     # new_messages = Message.objects.filter(sender=sender or receiver, receiver=receiver or sender)
#     context = {
#         'messages':messages,
#         'receiver_obj':receiver,
#     }
#     return render(request, 'src_code/message.html', context)


def savedPost(request, post_id, value):
    if request.method == 'POST':
        if value == 0:
            post = Post.objects.get(pk=post_id)
            post.saved.add(request.user)
        if value == 1:
            post = Post.objects.get(pk=post_id)
            post.saved.remove(request.user)
        return redirect('home-page')


def userPage(request, user_id):
    print(user_id)
    
    user = Detail.objects.get(user__id=user_id)
    user_post = User.objects.get(pk=user_id)
    tag_posts = Post.objects.filter(tag=user_id)
    print('tag posts', tag_posts)
    posts = Post.objects.filter(user=user_post)
    main_user = Detail.objects.get(user=request.user)

    context = {
        'user':user,
        'posts':posts,
        'main_user':main_user,
        'tags':tag_posts,
    }
    return render(request, 'src_code/user_page.html', context)

def likes(request):
    if request.method == 'POST':
        post_like_pk = request.POST['post_pk']
        post = Post.objects.get(pk=post_like_pk)

        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect('home-page')



def addPost(request):

    if request.method == 'POST':
        form = AddPosts(request.POST, initial={'user':request.user})
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = AddPosts(initial={'user':request.user})
        print(form)

    context = {
        'form':form,
    }
    return render(request, 'src_code/add_post.html', context)


def comments(request):

    
    return render(request, 'src_code.comments.html')



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        
        new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

        login(request, new_user)

        return redirect('home-page')
    else:
        form = UserRegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'src_code/register.html', context)



# details = Detail.objects.get(pk=1)
# # for detail in details:
# # for i in details.follwers:
# for i in details.followers.all():
#     print(i)
# print(details.followers.all())
tags_posts = Post.objects.filter(tag=4)

print(tags_posts, '---')