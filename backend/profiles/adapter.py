# from allauth.account.adapter import DefaultAccountAdapter
#
#
# class ProfileAccountAdapter(DefaultAccountAdapter):
#     def save_user(self, request, user, form, commit=False):
#         user = super().save_user(request, user, form, commit)
#         data = form.cleaned_data
#         # user.phone_number = data.get('phone_number')
#         user.name = data.get('name')
#         user.building = data.get('building')
#         user.room = data.get('room')
#         user.save()
#         return user