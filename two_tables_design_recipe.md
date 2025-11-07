# Two Tables Design Recipe Template

## 1. Extract nouns from the user stories or specification

>> Specification

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)

# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

>> Nouns:

album, title, release year, artist, name, genre

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                     |
| --------------------- | ------------------------------ |
| album                 | title, release year, artist_id |
| artist                | name, genre                    |

1. Name of the first table (always plural): `albums` 

    Column names: `title`, `release_year`, `artist_id`

2. Name of the second table (always plural): `artists` 

    Column names: `name`, `genre`

## 3. Decide the column types

>> Table: albums
id: SERIAL
title: text
release_year: int
artist_id: int

>> Table: artists
id: SERIAL
name: text
genre: text

## 4. Decide on The Tables Relationship

1. Can one artist have many albums? YES
2. Can one album have many artists? NO

-> Therefore,
-> An artist HAS MANY albums
-> An album BELONGS TO an artist

-> Therefore, the foreign key is on the albums table.

## 5. Write the SQL

>> file: music_library.sql

```sql

-- Create the table without the foreign key first.
CREATE TABLE artists (
  id SERIAL PRIMARY KEY,
  name text,
  genre text
);

-- Then the table with the foreign key second.
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int,
  constraint fk_artist foreign key(artist_id)
    references artists(id)
    on delete cascade
);

```

## 6. Create the tables

cd into seeds and run below bash command:

```bash
psql -h 127.0.0.1 music_library < music_library.sql
```
OR

Run 'python seed_dev_database.py'