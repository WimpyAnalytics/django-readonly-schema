
class LegacyDatabaseRouter(object):
    """
    This implements the Django DatabaseRouter protocol though we are using it to know which
    role to use for the same db and to turn off migrations.

    Though our underlying DB is new. We refer to this as "Legacy" because most of the time
    when someone is looking to turn off Django migrations it is because of an old/existing
    DB moving to a Django project that can then be managed by migrations. Not being allowed
    to change schema, we are the minority. Knowing this will help you google.

    The reader/writer roles most closely match a read slave/write master style setup so that
    is what you google for that.

    See: http://www.mechanicalgirl.com/post/reporting-django-multi-db-support/
    For a nice (but dated) example that is similar to what we want for reader/writer.

    As an aside, this is also good to know:
    http://stackoverflow.com/questions/2628431/in-django-how-to-create-tables-from-an-sql-file-when-syncdb-is-run
    """

    def db_for_read(self, model, **hints):
        """Typically for indicating a read slave. We use it to indicate the legacy db"""
        return 'legacy'

    def db_for_write(self, model, **hints):
        """Typically for indicating a master. We use it to indicate the 'writer' role"""
        return 'legacy'

    def allow_migrate(self, db, model):
        """This is the legacy bit"""
        return False

    def allow_relation(self, obj1, obj2, **hints):
        """This is ok as we don't actually have multiple databases"""
        return True
