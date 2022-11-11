text = '''On January 8, Prince Harry and Meghan Markle, the Duke and Duchess of Sussex, unveiled their controversial plan to walk away from royal roles. We intend to step back as 'senior' members of the royal family and work to become financially independent while continuing to fully support her majesty the queen, they said in a joint statement. We now plan to balance our time between the United Kingdom and North America, continuing to honor our duty to the Queen, the commonwealth and our patronages. This geographic balance will enable us to raise our son with an appreciation for the royal tradition into which he was born, while also providing our family with the space to focus on the next chapter, including the launch of our new charitable entity, the statement added. Apparently, the announcement on the Sussex Royal Instagram page blindsided the Queen and other family members who had no idea it was coming, it sent tabloids into overdrive. Meanwhile, the Queen summoned Senior Royals to an emergency summit to discuss the future of the Duke and Duchess of Sussex. Billed as the Sandringham summit, the meeting took place at the Queen's estate in Norfolk and involved Queen Elizabeth II, Harry his father, Prince Charles and his brother Prince William, with Meghan Markle reportedly joining the discussions by phone from Canada. Soon after, the queen released a statement, that said, My family and I are entirely supportive of Harry and Meghan Markle desire to create a new life as a young family. Although we would have preferred them to remain full-time working members of the Royal family, we respect and understand their wish to live a more independent life as a family while remaining a valued part of my family.'''

list_of_keyphrases = ['Prince Charles', 'Prince William', 'Meghan Markle', 'United Kingdom', 'North America', 'Duke and Duchess of Sussex', 'Queen Elizabeth II']

for key in list_of_keyphrases:
    replace_with = key.replace(' ', '_')
    text = text.replace(key, replace_with )
print(text)