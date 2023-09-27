# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")


# Tasas de cambio
def obtener_tasas_de_cambio():
  return {
      'COP': 4106,  # 1 USD = 4106 COP
      'CLP': 909,  # 1 USD = 909 CLP
      'MXN': 18,  # 1 USD = 18 MXN
      'USD': 1,  # 1 USD = 1 USD
      'RUB': 96  # 1 USD = 96 RUB
  }


# Inicializar variables
tasas_de_cambio = obtener_tasas_de_cambio()
monedas = list(tasas_de_cambio.keys())
historial = []


# Menú
def mostrar_menu():
  print("\n🌟 Menú:")
  print("1. Mostrar Monedas 🪙")
  print("2. Mostrar Tasas de Cambio 💱")
  print("3. Establecer Monedas 🔄")
  print("4. Realizar Conversión 💰")
  print("5. Ver Historial 📜")
  print("6. Salir 🚀")


# Obtener moneda desde consola
def obtener_moneda(mensaje):
  while True:
    moneda = input(mensaje).upper()
    if moneda in monedas:
      return moneda
    else:
      print("❌ Moneda no válida. Inténtalo nuevamente.")


# Obtener cantidad desde consola
def obtener_cantidad():
  while True:
    cantidad_str = input("Ingrese la cantidad a convertir 💲: ")
    try:
      cantidad = float(cantidad_str)
      return cantidad
    except ValueError:
      print("❌ Cantidad no válida. Inténtalo nuevamente.")


# Conversión
def realizar_conversion():
  mostrar_tasas_de_cambio()
  moneda_base = obtener_moneda("Ingrese la moneda base 🪙: ")
  moneda_objetivo = obtener_moneda("Ingrese la moneda objetivo 🪙: ")
  cantidad = obtener_cantidad()

  tasa_base = tasas_de_cambio[moneda_base]
  tasa_objetivo = tasas_de_cambio[moneda_objetivo]

  resultado = cantidad * (tasa_objetivo / tasa_base)

  print(
      f"\n💲 {cantidad} {moneda_base} equivale a 💲 {resultado:.2f} {moneda_objetivo}"
  )
  historial.append(
      f"{cantidad} {moneda_base} -> {resultado:.2f} {moneda_objetivo}")


# Mostrar las tasas de cambio
def mostrar_tasas_de_cambio():
  print("\n📊 Tasas de Cambio Actuales:")
  for moneda, tasa in tasas_de_cambio.items():
    print(f"{moneda}: 1 USD = {tasa} {moneda}")


# Ver el historial
def ver_historial():
  print("\n📜 Historial de Conversiones:")
  for registro in historial:
    print(registro)


# Ejecución del programa
while True:
  mostrar_menu()
  opcion = input("Seleccione una opción: ")

  if opcion == '1':
    print("\n🪙 Monedas Disponibles:")
    print(", ".join(monedas))
  elif opcion == '2':
    mostrar_tasas_de_cambio()
  elif opcion == '3':
    print("\n🔄 Establecer Monedas:")
    moneda_base = obtener_moneda("Moneda base 🪙: ")
    moneda_objetivo = obtener_moneda("Moneda objetivo 🪙: ")
    print(f"\n✅ Monedas establecidas: {moneda_base} -> {moneda_objetivo}")
  elif opcion == '4':
    realizar_conversion()
  elif opcion == '5':
    ver_historial()
  elif opcion == '6':
    print("\n🚀 ¡Adiós!")
    break
  else:
    print("\n❌ Opción no válida. Inténtalo nuevamente.")
