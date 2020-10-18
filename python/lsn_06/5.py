'''5. Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.'''


class Computer:
    count = 0

    def inst(self, processor: str, ssd: int, ram: int, video="Nvidia"):
        print(f"Собираем ПК")
        self.processor = processor
        self.ssd = ssd
        self.ram = ram
        self.video = video
        Computer.count+=1


pc1 = Computer()
pc2 = Computer()
pc1.inst("Core i3", 120, 16, "AMD")
pc2.inst("Celeron",250,8)

print(pc1.processor, pc1.ssd, pc1.ram, pc1.video)
print(pc2.processor, pc2.ssd, pc2.ram, pc2.video)
print(pc1.count)