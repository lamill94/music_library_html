# Plain Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

POST /albums
    title: string
    release_year: number (str)
    artist_id: number (str)

GET /albums

## 2. Create Examples as Tests

a. Go through each route and write down one or more example responses.
b. Remember to try out different parameter values.
c. Include the status code and the response body.

>> Scenario 1:

# POST /albums
#   title: "Baltimore"
#   release_year: 1978
#   artist_id: 4
# Expected response (200 OK)
no content

# GET /albums
# Expected response (200 OK)
Album(1, Surfer Rosa, 1988, 1)
Album(2, Doolittle, 1989, 1)
Album(3, Ring Ring, 1973, 2)
Album(4, Waterloo, 1974, 2)
Album(5, Lover, 2019, 3)
Album(6, Folklore, 2020, 3)
Album(7, I Put a Spell on You, 1965, 4)
Album(8, Here Comes the Sun, 1971, 4)
Album(9, Baltimore, 1978, 4)

>> Scenario 2

# POST /abums
# Expected response (400 Bad Request)
You need to submit a title, release_year and artist_id

# GET /albums
# Expected response (200 OK)
Album(1, Surfer Rosa, 1988, 1)
Album(2, Doolittle, 1989, 1)
Album(3, Ring Ring, 1973, 2)
Album(4, Waterloo, 1974, 2)
Album(5, Lover, 2019, 3)
Album(6, Folklore, 2020, 3)
Album(7, I Put a Spell on You, 1965, 4)
Album(8, Here Comes the Sun, 1971, 4)

## 3. Test-drive the Route

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

```python



```

