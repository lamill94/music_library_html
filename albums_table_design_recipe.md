## 1. Extract nouns from the user stories or specification

>> Specification:

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

>> Nouns:

album, title, release year, artist_id

## 2. Infer the Table Name and Columns

| Record                | Properties                     |
| --------------------- | ------------------------------ |
| album                 | title, release year, artist_id |

Name of the table (always plural): `albums`

Column names: `title`, `release_year`, `artist_id`

## 3. Decide the column types

id: SERIAL
title: text
release_year: int
artist_id: int

## 4. Write the SQL

>> file: music_library.sql

```sql

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);

```

## 5. Create the table

cd into seeds and run below bash command:

```bash
psql -h 127.0.0.1 music_library < music_library.sql
```

OR 

python seed_dev_database.py