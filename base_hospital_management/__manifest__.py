{
    'name': 'Hospital Management',
    'description': """
        Hospital management module which is used to mange the hospital functionalities prescription,patient,doctor diagnosis etc
    """,
    'summary': """
    Hospital management module which is used to mange the hospital functionalities prescription,patient,doctor diagnosis etc
""",
    'author' : 'Rakib Hasan',
    'license' : 'AGPL-3',
    'category' : 'Hospital',
    'version' : '13.0.1.0,2',
    'depends' : [],
    'data' : [
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/views_bed.xml',
        'views/views_ward.xml',
        'views/views_hospital.xml',
    ],
    'installable':True,
    'application':True,
}
