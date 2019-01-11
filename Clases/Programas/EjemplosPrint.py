i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # minimum field
# imprime 62 como un string
print '"%5d"' % i      # field of width 5 characters
# imprime 62 como string y deja 3 caracteres vacios a la izquierda ya que pide que muestre 5 de ellos pero solo hay dos
print '"%05d"' % i     # pad with zeros
# imprime 62 como string y hace lo mismo que el anterior solo que en vez de dejar espacios vacios los llena con ceros
print '"%g"' % r       # r is big number so this is scientific notation
# imprime  1.89877e+08 como string en notacion cientifica con menos decimales
print '"%G"' % r       # E in the exponent
# imprime  1.89877E+08 como string en notacion cientifica con menos decimales
print '"%e"' % r       #compact scientific notation
# imprime  1.898765e+08 como notacion cientifica con mas decimales MAS PRECISION
print '"%E"' % r       # compact scientific notation
# imprime  1.898765e+08 como notacion cientifica con mas decimales MAS PRECISION
print '"%20.2E"' % r   # 2 decimals, field of width 20
# imprime la cadena "            1.90E+08" que deja un expacio de 12 caracteres ya que ya teniamos 8 con un total de 20 y solo deja 2 decimales
print '"%30g"' % r     # field of width 30 (right-adjusted)
# imprime "                   1.89877e+08" usa 30 caracteres haciendo los decimales muy chicos
print '"%-30g"' % r    # left-adjust number
# imprime lo mismo que el anterior solo que en vez de dejar caracteres vacios a la izquierda los deja a la derecha
print '"%-30.4g"' % r  # 3 decimals
# imprime  dejando 3 decimales y espacios restantes a la derecha
print '%s' % i   # can convert i to string automatically
# convierte 62 en cadena sin necesidad de usar comillas
print '%s' % r
# lo mismo que el de ARRIBA solo que con r
# Use %% to print the percentage sign
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)
# imprime 5.1 % of 346.00 Euro is 17.65 Euro ya que todo lo hace cadena
