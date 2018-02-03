from McdonaldsApi import McDonald

# Create a new api object
m = McDonald()

# Returns object containing restaurant location, images, description
m.get_restaurants()

# Returns items u can buy and their image and description
m.get_foods()

# Returns random news and stuff that app uses
m.get_content()