# Переменные запросов Битрикс24
BX24__COUNT_RECORDS_IN_METHODS = 5      # должно быть 50
BX24__COUNT_METHODS_IN_BATH = 5

COUNT_THREAD = 1

# способы поиска дубликатов
DUPLICATES_FIELDS = {
    'email_company': ['EMAIL__VALUE', 'companies__TITLE'],
    'email_contact_name': ['EMAIL__VALUE', 'NAME'],
}

# способы объединения полей контактов
TYPE_MERGE_FIELD = {
    # 'max_length': ['NAME', ],
    'max_length': ['NAME', ],
    # 'concat_asc_date': [],
    'concat_asc_date': ['SOURCE_DESCRIPTION', 'UF_CRM_1662986623502', 'UF_CRM_1662986639015', 'UF_CRM_1662986876354', 'UF_CRM_1662984604'],
    # 'concat_desc_date': ['LAST_NAME', ],
    'concat_desc_date': ['UF_CRM_1662984465', ],
    # 'multi_field': ['EMAIL', 'PHONE', ]
    # 'multi_field': ['EMAIL', 'PHONE', ]
}

