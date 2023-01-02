# BASE_DONNE => SERVER => CLIENT ( NAVIGATEUR ) / CODE APPEL API
# BASE_DONNE: ( MySQL, PostgreSQL, Sqlite, Oracle )
# SQL, NoSQL
# ENTREPOT DE DONNEES: ( datawarehouse, datacenters )
# SERVER: ( LINUX: Ubuntu, Debian, RedHat, Windows )
# CLIENT: ( Application WEB, Application Desktop, SCript Python)


# UEMOA et CEMAC
# amount ( UEMOA <=> CEMAC )

# EUR => XOF ( 655,957 )
# USD => XOF ( 610,500 )

# EUR ( France, Italie )
# USD ( Congo, Etats Unis )
# XOF ( Senegal, Mali )

#  Senegal => France ( XOF => EUR ) ( 200 ) ( 2E )
#  Mali => France ( XOF => EUR ) ( 200 ) ( 2E )
#  Burkina => France ( XOF => EUR ) ( 200 ) ( 2E )
#  Senegal => USA ( XOF => USD ) ( 200 ) ( 2E )

# { 'XOF': { 'USD': 11.66, 'EUR': 22.98 } }
# { 'USD': { 'XOF': 38.88, 'EUR': 47.99 } }
# { 'EUR': { 'USD': 5, 'XOF': 6 } }

# convertor(200, 'XOF', 'USD)


convert_xof_to_eur = 200 / 655.957
convert_xof_to_usd = 200 / 610.500

convert_eur_to_xof = 2 * 655.957
convert_usd_to_usd = 2 * 610.500


BASE_DE_DONNES = {
    'XOF': {
        {
            'USD': 11.66,
            'EUR': 22.98
        }
    },
    'USD': {
        {
            'XOF': 38.88,
            'EUR': 47.99,
        }
    },
    'EUR': {
        {
            'USD': 138.88,
            'XOF': 28.86,
        }
    },
}


def convertor(
    amount: float,
    start_currency: str,
    final_currency: str
) -> float:
    
    if start_currency == final_currency:
        return amount
    
    change = BASE_DE_DONNES \
        .get(start_currency) \
        .get(final_currency)
        
    return amount * change



names = ['Orange', 'Banane', 'Tomate', 'Piment']


def pluralize(name: str):
    return f'{name}s'


# EXCEL avec 1000 Employees
def update_salary(salary: float):
    return salary + 1000

for name in names:
    print(pluralize(name))
    