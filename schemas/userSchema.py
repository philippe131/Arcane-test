from schemas import ma

#  User schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'date_birth')

# Init UserSchema
user_schema = UserSchema()
users_schema = UserSchema(many=True)
