def get_formmated_city_country(city, country, population=''):
    '''生成格式规范的城市国家'''
    if population:
        full_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        full_name = f"{city.title()} {country.title()}"
    return full_name