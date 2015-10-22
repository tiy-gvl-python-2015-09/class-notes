# Migrations

In order to create/remove/update date in a scripted automated fashion -or- change the structure of your models
(for example, adding or removing a field on a class) you will need to generate a migration and run that
migration.  The order for this process is as follows:

## For a Schema (structure) Migration

* Make the change in your `models.py` file
* Generate a migration from the command line or PyCharm's manage.py console. `manage.py makemigrations <appname>`
* If no errors - run the migration with `manage.py migrate`

## For a Data Migration

* Generate an empty migration from the command line or PyCharms manage.py console. `manage.py makemigrations <appname> --empty`
* Create the function to read and create or update or delete your data in your database.
* add a `migrations.RunPython(yourfunctionname)` in the `operations` list on the `Migration` class.
* If no errors - run the migration with `manage.py migrate`

# Querying and Creating Data

### Querying for Data

When you search for data in your database and you only expect or want a single instance of that model back
you would want to use `ModelName.objects.get(...)`.  If you want or expect multiple results to be returned
(for example you may want every shirt with a color of `green`) you would use `ModelName.objects.filter(...)`.

A big difference between `get()` and `filter()` is that if the `get` encounters any trouble it will raise
an exception.  So if you are trying to do a `get` on a value that doesn't exist in the database - you're
in for a bad time.  However with a `filter()` it will fail gracefully and just give you an empty list.

### Creating Data

When you want to create data the quickest way to do so is with a `ModelName.objects.create(...)` command.
You can run this in a function in a migration, from a django shell (`manage.py shell`), or even a view!
