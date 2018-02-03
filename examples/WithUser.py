from McdonaldsApi import McDonald

m = McDonald()

# Register a new account
m.register('Janez', 'Novak', 'janez.novak@example.com', 'janeznovak1')

# After you confirm the mail you can login
m.login('janez.novak@example.com', 'janeznovak1')

# Now you can lookup your info
m.get_user_info()

# Get your coupons
m.get_coupons()

# Try to get a joker coupon which I never seen work after 50+ attempts
m.play_joker()

# Check in a qr code from reciept
m.record_checkin('037586070774885501441724809368881162086868782551801101636126')
