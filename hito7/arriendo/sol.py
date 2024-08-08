import json

data = [
    {
        "model": "chilestay.inmueble",
        "pk": 1,
        "fields": {
            "id": "1",
            "nombre": "Hotel Vista Hermosa",
            "arrendada": False,
            "direccion": "Calle del Sol 456, Santiago, Chile",
            "comuna": 1,
            "region": 1,
            "tipo_inmueble": 1,
            "servicios": {
                "wifi": True,
                "aire_acondicionado": True,
                "zona_trabajo": True,
                "cocina": True,
                "calefaccion": True,
                "televisor": True,
                "piscina": True,
                "gimnasio": True
            },
            "calificacion_sernatur": {
                "sello_calidad": True,
                "sello_sustentabilidad": False,
                "compromiso_practicas": True
            },
            "telefono": "+56 2 1234 5678",
            "correo_electronico": "contacto@vistahermosa.cl",
            "pagina_web": "https://www.vistahermosa.cl",
            "descripcion": "Hotel confortable con vistas panorámicas y servicios completos.",
            "usuarios": [1]
        }
    },
    {
        "model": "chilestay.inmueble",
        "pk": 2,
        "fields": {
            "id": "2",
            "nombre": "Hostal Andes",
            "arrendada": False,
            "direccion": "Avenida Libertador 123, Valparaíso, Chile",
            "comuna": 2,
            "region": 2,
            "tipo_inmueble": 2,
            "servicios": {
                "wifi": True,
                "aire_acondicionado": False,
                "zona_trabajo": True,
                "cocina": True,
                "calefaccion": True,
                "televisor": False,
                "piscina": False,
                "gimnasio": False
            },
            "calificacion_sernatur": {
                "sello_calidad": False,
                "sello_sustentabilidad": True,
                "compromiso_practicas": False
            },
            "telefono": "+56 2 2345 6789",
            "correo_electronico": "info@hostalandes.cl",
            "pagina_web": "https://www.hostalandes.cl",
            "descripcion": "Un acogedor hostal en el corazón de Valparaíso.",
            "usuarios": [2]
        }
    },
    {
        "model": "chilestay.inmueble",
        "pk": 3,
        "fields": {
            "id": "3",
            "nombre": "Cabañas del Bosque",
            "arrendada": True,
            "direccion": "Camino del Bosque 789, Pucón, Chile",
            "comuna": 3,
            "region": 3,
            "tipo_inmueble": 3,
            "servicios": {
                "wifi": True,
                "aire_acondicionado": False,
                "zona_trabajo": False,
                "cocina": True,
                "calefaccion": True,
                "televisor": True,
                "piscina": True,
                "gimnasio": False
            },
            "calificacion_sernatur": {
                "sello_calidad": True,
                "sello_sustentabilidad": True,
                "compromiso_practicas": True
            },
            "telefono": "+56 2 3456 7890",
            "correo_electronico": "reservas@cabanasdelbosque.cl",
            "pagina_web": "https://www.cabanasdelbosque.cl",
            "descripcion": "Cabañas acogedoras rodeadas de naturaleza.",
            "usuarios": [3]
        }
    },
    
]

with open('inmuebles.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Archivo inmuebles.json generado exitosamente.")
