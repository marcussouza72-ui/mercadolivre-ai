from app.auth.hashing import hash_password, verify_password

senha = "12345678"

hash_gerado = hash_password(senha)

print("HASH:")
print(hash_gerado)

print()

print("VERIFY:")
print(verify_password(senha, hash_gerado))