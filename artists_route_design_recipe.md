# Plain Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

POST /artists
    name: string
    genre: string

GET /artists

## 2. Create Examples as Tests

a. Go through each route and write down one or more example responses.
b. Remember to try out different parameter values.
c. Include the status code and the response body.

>> Scenario 1:

# POST /artists
#   name: "Wild Nothing"
#   genre: "Indie"
# Expected response (200 OK)
no content

# GET /artists
# Expected response (200 OK)
Artist(1, Pixies, Rock)
Artist(2, ABBA, Pop)
Artist(3, Taylor Swift, Pop)
Artist(4, Nina Simone, Jazz)
Artist(5, Wild Nothing, Indie)

>> Scenario 2

# POST /artists
# Expected response (400 Bad Request)
You need to submit a name and genre

# GET /artists
# Expected response (200 OK)
Artist(1, Pixies, Rock)
Artist(2, ABBA, Pop)
Artist(3, Taylor Swift, Pop)
Artist(4, Nina Simone, Jazz)

## 3. Test-drive the Route

After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.

```python



```

