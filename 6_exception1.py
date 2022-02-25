"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
i = 0
for i in range(1):
  try:
    def hello_user(feel):
      while feel != 'Хорошо':
        feel = input('Как дела?')
    
    feel = input('Как дела?')

    if __name__ == "__main__":
      hello_user(feel)

  except KeyboardInterrupt:
    print("Пока!")
    break
  


