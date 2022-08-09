from tkinter import CASCADE
from django.db import models

# Create your models here.

class Race(models.Model):
    '''The race/ethnicity of a person. Used for both authors and characters.
        Attributes:
            name (CharField): A name of a race such as "Black" or "Asian"
            description (CharField): Optional. Used if clarification of name/
                authoritative language is needed. May include alternative names for 
                the race.
    '''
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Gender(models.Model):
    '''The gender of a person, as they self-identify. Used for both authors and characters.
        Attributes:
            name (CharField): A name of a gender (i.e. 'male', 'female', 'other')
            description (CharField): Optional. Used if clarification of name/
                authoritative language is needed. May include alternative names for
                the gender.
    '''
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Characters(models.Model):
    """The main characters from a work represented by the count of identities present. Attributes
        are determined by publicly available information from the publisher and/or review websites.
            Attributes:
                book_title (CharField): The title of the book the characters are from. UPPER CASE.
                non_humans (IntegerField): Number of main characters that are an animal, robot, or non-humanoid. Sci fi or fantasy
                    characters that are of a humanoid race are considered human.
                plus_size (IntegerField): Count of characters described as fat or considered "overweight".
                lgbtqia (IntegerField): Count of characters identifying themselves as having a non-cis gender identity
                    or non-straight sexual orientation.
                immigrants (IntegerField): Count of characters that have experienced moving to a country other than their home country.
                neurodiverse (IntegerField): Count of characters that have a neurodiverse identity such being autistic, having
                    attention-deficit hyperactivity disorder, or having another brain-based difference that they do not
                    consider to be a disability.
                disabled (IntegerField): Count of characters identifying as disabled or as having a chronic illness.
                experiencing_homelessness_low_income (IntegerField): Count of characters that do not have a permanent home or
                    are experiencing poverty.
                adverse_mental_health_trauma_response (IntegerField): Count of characters living with poor mental health or
                    experiencing a traumatic event (relative to the other individuals in their world).
                addiction (IntegerField): Count of characters experiencing addiction themselves or has a loved one experience
                    addiction.
                notes (CharField): Optional. Notes that are relevant specifically to the characters in the book.
    """
    book_title = models.CharField(max_length=100, null=True)
    non_humans = models.IntegerField(null=True, verbose_name='Number of non-human characters')
    plus_size = models.IntegerField(null=True, verbose_name='Number of plus-size characters')
    lgbtqia = models.IntegerField(null=True, verbose_name='Number of LGBTQIA+ characters')
    immigrants = models.IntegerField(null=True, verbose_name='Number of characters who are immigrants')
    neurodiverse = models.IntegerField(null=True, verbose_name='Number of neurodiverse characters')
    disabled = models.IntegerField(null=True, verbose_name='Number of disabled characters')
    experiencing_homelessness_low_income = models.IntegerField(null=True, verbose_name='Number of characters who are experiencing homelessness or low-income')
    adverse_mental_health_trauma_response = models.IntegerField(null=True, verbose_name='Number of characters who are experiencing adverse mental health or trauma response')
    addiction = models.IntegerField(null=True, verbose_name='Number of characters who are experiencing addiction')
    notes = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"From {self.book_title}"

class CharRaceConn(models.Model):
    '''This is an intermediate class representing the relationship between a set of characters
    and a race.
        Attributes:
            quantity (IntegerField): The number of characters from the character set of the selected race
        Relationships:
            race (Race object, ForeignKey): The selected race for this relationship.
            character_set (Characters object, ForeignKey): The Characters object that contains the
                        described characters.
    '''
    quantity = models.IntegerField(null=True)
    race = models.ForeignKey(Race, null=True, on_delete=models.CASCADE)
    character_set = models.ForeignKey(Characters, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} {self.race} characters'
        # Consider changing to include book title if finding CharRaceConn objects in admin panel becomes an issue

class CharGenderConn(models.Model):
    '''This is an intermediate class representing the relationship between a set of characters
    and a gender.
        Attributes:
            quantity (IntegerField): The number of characters from the character set of the selected gender
        Relationships:
            gender (Gender object, ForeignKey): The selected gender for this relationship.
            character_set (Characters object, ForeignKey): The Characters object that contains the
                        described characters.
    '''
    quantity = models.IntegerField(null=True)
    gender = models.ForeignKey(Gender, null=True, on_delete=models.CASCADE)
    character_set = models.ForeignKey(Characters, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} characters of {self.gender} gender'
        # Consider changing to include book title if finding CharGenderConn objects in admin panel becomes an issue

class Genre(models.Model):
    '''The genre of a book.
        Attributes:
            name (CharField): A name of a genre (e.g. 'Contemporary', 'Fantasy', etc.)
            description (CharField): Optional. Used if clarification of name/
                authoritative language is needed. May include alternative names for
                the genre.
    '''
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class ShelvingCategory(models.Model):
    '''The physical location of a book in our library. "Duplicate" entries recommended if
    multiple copies of the book are shelved in different locations.
        Attributes:
            name (CharField): A name of a shelving category (e.g. 'Juvenile Fiction', 'Visual Arts', etc.)
            description (CharField): Optional. Used if clarification of name/
                authoritative language is needed. May include alternative names for
                the shelving category.
    '''
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    """A book or other information resource (here referred to as 'book'). Attributes are determined by publicly
        available information from the publisher and/or review websites.
            Attributes:
                title (CharField): The title of the book. UPPER CASE.
                genres (Genre object, ManyToManyField): The genre(s) of the book.
                shelving_category (ShelvingCategory object, ForeignKey): The shelving location of the book in our library.
                is_ownvoice (BooleanField): True if the characters are very similar to the author's own lived experience. Only
                    includes non-traumatic/joyful ownvoice narratives.
                is_not_in_USA (BooleanField): True if the main action of the plot takes place in a place other than the United States.
                    False if the location is in the US or a fantasy/unreal world.
                is_verse (BooleanField): True if the book is written in the style of poetry, not prose.
                from_independent_publisher (BooleanField): True if the book is from a small, independent publisher.
                characters (Characters object, OneToOneField): an object representing the set of main characters (most typically one)
                                from the book. Attributes of this object describe how many of each type of character exist in the book.
                notes (CharField): Any other notes found to be revelant to the book specifically (not author or characters).
    """
    title = models.CharField(max_length=200, null=True)
    genres = models.ManyToManyField(Genre)
    shelving_category = models.ForeignKey(ShelvingCategory, null=True, on_delete=models.SET_NULL)
    is_ownvoice = models.BooleanField()
    is_not_in_USA = models.BooleanField()
    is_verse = models.BooleanField(verbose_name='Is written in verse')
    from_independent_publisher = models.BooleanField()
    characters = models.OneToOneField(Characters, on_delete=models.CASCADE, null=True)
    notes = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    """An author of a book. Attributes are determined based on the information on the author's or
        publisher's website.
            Attributes:
                first_name (CharField): The author's first or given name. ALL CAPS.
                last_name (CharField): The author's last or family name. ALL CAPS.
                full_name (CharField): The author's full name.
                races (Race object, ManyToManyField): One or more races describing the author.
                gender (Gender object, ForeignKey): The gender of the author. Genders are based on self-identification. A trans
                    individual is not 'other,' rather, include this identity under is_lgbtqia.
                non_marginalized (BooleanField): True if the author is race=white and not neurodiverse, disabled,
                    lgbtqia, or an immigrant. Otherwise, False.
                uses_ownvoice (BooleanField): True if the author writes characters that are very similar to their own lived experience.
                is_immigrant (BooleanField): True if the author experienced moving to a country other than their home country.
                is_neurodiverse (BooleanField): True if the author has a neurodiverse identity such being autistic, having
                    attention-deficit hyperactivity disorder, or having another brain-based difference that they do not
                    consider to be a disability.
                is_disabled (BooleanField): True if the author identifies as disabled or has a chronic illness.
                is_lgbtqia (BooleanField): True if the author identifies themselves as having a non-cis gender identity or non-straight
                    sexual orientation.
                notes (CharField): Any other notes found to be revelant to the author specifically (not book or characters).
                books (Book object, ManyToManyField): Book objects that the author has written or co-written.
            Functions:
                __init__: Initializes an object of the Author class.
                __str__: String representation of the object.
                add_book: Adds a Book object to the list of books by this author.
    """
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    full_name = models.CharField(max_length=200, null=True)
    races = models.ManyToManyField(Race)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    non_marginalized = models.BooleanField()
    uses_ownvoice = models.BooleanField()
    is_immigrant = models.BooleanField()
    is_neurodiverse = models.BooleanField()
    is_disabled = models.BooleanField()
    is_lgbtqia = models.BooleanField()
    notes = models.CharField(max_length=500, null=True, blank=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.full_name