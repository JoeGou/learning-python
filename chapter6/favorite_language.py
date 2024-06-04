favorite_languages = {
    'jen': ['python', 'c'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}

for name, language in favorite_languages.items():
    if len(language) >= 2:
        
        print(f"{name.title()}'s favorite languages are:")
        for language in language:
            print(f"\t{language.title()}")
    else:
        print(f"{name.title()}'s favorite languages is:")
        for language in language:
            print(f"\t{language.title()}")    