import json

tipos_inmueble = [
    {
        "model": "chilestay.tipoinmueble",
        "pk": 1,
        "fields": {
            "nombre": "Hotel"
        }
    },
    {
        "model": "chilestay.tipoinmueble",
        "pk": 2,
        "fields": {
            "nombre": "Hostal"
        }
    },
    {
        "model": "chilestay.tipoinmueble",
        "pk": 3,
        "fields": {
            "nombre": "Cabaña"
        }
    },
    {
        "model": "chilestay.tipoinmueble",
        "pk": 4,
        "fields": {
            "nombre": "Departamento"
        }
    },
    {
        "model": "chilestay.tipoinmueble",
        "pk": 5,
        "fields": {
            "nombre": "Casa"
        }
    },
    {
        "model": "chilestay.tipoinmueble",
        "pk": 6,
        "fields": {
            "nombre": "Apartamento"
        }
    },
    # Añadir más entradas aquí si es necesario
]

with open('tipos_inmueble.json', 'w', encoding='utf-8') as f:
    json.dump(tipos_inmueble, f, ensure_ascii=False, indent=4)

print("Archivo tipos_inmueble.json generado exitosamente.")
