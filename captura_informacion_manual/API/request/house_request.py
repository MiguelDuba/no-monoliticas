

class CreateHouse(BaseCommannd):
  def __init__(self, username, password, email, dni, fullName, phoneNumber):
    self.username=username
    self.password=password
    self.email=email
    self.dni=dni
    self.fullName=fullName
    self.phoneNumber=phoneNumber

  def execute(self):
    u = User(self.username, self.email, self.phoneNumber, self.dni, self.fullName, self.password,"POR_VERIFICAR")
    db_session.add(u)
    
    if (self.username=="" or self.email=="" or self.password=="" or self.username is None or self.email is None or self.password is None ):
      raise InvalidParams
    
    else:
      try:
        db_session.commit()
        response={"id":u.id, "createdAt":u.createdAt}
        db_session.close()
        #Funcion - Native/Verifiy.
        # CreateUser.CreateTaskVerify(self, str(u.id))

        return response
      except IntegrityError  as e:
        if isinstance(e.orig, UniqueViolation):
          db_session.close()
          raise EmailUsernameExist