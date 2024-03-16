

## Lab One

Create a YAML file that satisfies the following requirements:

Create a file called config.yaml

#### Create a Database Host Mapping
Create a top-level mapping key called database that contains a mapping key called host with the value `db.example.net`

#### Create a Port Mapping
Under the database key, add a mapping key called `port` with the value `3306`

#### Create a Enabled Mapping
Under the database key, add a mapping key called `enabled` with the value `true`

#### Create a Legacy Mapping
Under the database key, add a mapping key called `legacy` with the value `yes`


#### Re-use the Database Configuration
Re-use the database mapping data so that the following are satisfied:

A new top-level mapping called `database_new` exists
The `database` mapping has an anchor called `common`
The `database_new` mapping has an alias called `common`



---

## Lab Two
Convert the following YAML to JSON format and save it to a file called `xmas.json`

```yaml
---
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
```

---

## Lab Three

Convert the following JSON to YAML format and save it to a file called `heroes.yaml`


```json
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```






