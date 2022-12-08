# arff-generator

*Read this in [Español](README.es.md).*

An **ARFF** (*Attribute-Relation File Format* — the dataset format used by [Weka](https://www.cs.waikato.ac.nz/ml/weka/)) file generator that produces randomized data from the attributes and values you define.

Handy for quickly creating test datasets without writing the `.arff` by hand.

## Requirements

- Python 3.6+ (standard library only: `random`, `os`)

## Usage

Define the relation, the attributes with their possible values, and the classification attribute, then call `randomize()`:

```python
from arffclass import *

file = arffGenerator()
file.setDatas(20)                  # number of data rows to generate
file.setRelation("meteoritos")     # relation name
file.setFileName("prueba")         # output file name (.arff is appended)

# possible values of the classification attribute
file.setClass(["Coronis", "Eos", "Temis", "Flora", "Maria"])

# attribute and its possible values
file.setAttribute("tiporoca", ["arcilla", "niquel", "hierro", "desconocido"])
file.setAttribute("diametro", [1, 2, 3, 4, 5])
file.setAttribute("masa", [2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3])
file.setAttribute("forma", ["dentada", "irregular"])
file.setAttribute("riezgoimpacto", ["bajo", "medio", "alto"])

file.randomize()   # generates the .arff file with random data
```

Run:

```bash
python main.py
```

Generates `output/prueba.arff`. The `output/` folder is created automatically; if the file already exists, it is overwritten.

## Example output

```
@relation meteoritos

@attribute tiporoca {arcilla, niquel, hierro, desconocido}
@attribute diametro {1, 2, 3, 4, 5}
@attribute masa {2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3}
@attribute forma {dentada, irregular}
@attribute riezgoimpacto {bajo, medio, alto}
@attribute class {Coronis, Eos, Temis, Flora, Maria}

@data
desconocido, '5', '3.1', dentada, alto, Temis
arcilla, '3', '3.1', irregular, bajo, Flora
hierro, '5', '3.2', irregular, medio, Eos
hierro, '2', '2.9', irregular, bajo, Maria
niquel, '3', '2.7', irregular, alto, Eos
niquel, '4', '2.9', irregular, medio, Temis
desconocido, '5', '3.1', dentada, alto, Maria
hierro, '3', '2.9', irregular, bajo, Flora
...
```

> Numeric values are written in single quotes (`'3'`) so Weka treats them as nominal, like the rest of the attributes.

![Generated meteoritos.arff opened in an editor](screenshot.jpg)

## API — `arffGenerator`

| Method | Description |
|--------|-------------|
| `setDatas(int)` | Number of data rows to generate |
| `setRelation(str)` | Relation name (`@relation`) |
| `setFileName(str)` | Output file name (`.arff` is appended) |
| `setClass([...])` | Possible values of the `class` classification attribute |
| `setAttribute(name, [...])` | Adds an attribute and its list of possible values |
| `randomize()` | Generates the `.arff` file with the random data |

Each `set*` validates the input type and raises an exception if it is wrong (e.g. `setDatas` requires `int`, `setAttribute` requires a `list` of values).

## Files

| File | Purpose |
|------|---------|
| [arffclass.py](arffclass.py) | `arffGenerator` class (reusable API) |
| [main.py](main.py) | Example using the class |
| [simpleconsole.py](simpleconsole.py) | Standalone script version, no class (configured via variables) |

## Notes

- `simpleconsole.py` ships with `datas = 10000000` by default — would generate a huge file. Adjust that value before running it.
- The classification attribute name is always `class`; `randomize()` adds it automatically from `setClass()`.
