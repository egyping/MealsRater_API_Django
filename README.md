# MealsRater_API_Django

# Business requirements as per the mockup 

1- Meals list screen has the foloowing information
    - Meal name
    - Meal number of stars 
    - Meals average rate 
    - Login 
    - Register
    - showing already logged in user 

2- Popup error if the user already rated 

3- Add rate scree, stars 1 to 5 only and SAVE


# Technical requirements 
Using Django REST frame work please implement the followings

1- Models 
    - Meal
    - Stars 
    - User

2- validation if the user already rated the meal 

3- validation to rate min 1 and max 5 

4- CRUD API for Meals 
    http://127.0.0.1:8000/api/meals
    it should return the average rating and number of rating a long with the meal name and detail

5- CRUD API for Stars 
    http://127.0.0.1:8000/api/stars
    no one should be able to use this crud for rating !!

6- Rate API 
    http://127.0.0.1:8000/api/meals/meal_pk/rate_meal
    create and update API 

7- Token authentication 

8- Login and register API 

9- Token request API 

10- Deploy to Heroku 

