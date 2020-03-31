"""
Напишите генератор get_frames(), который производит «оконную
декомпозицию» сигнала: на основе входного списка генерирует набор
списков – перекрывающихся отдельных фрагментов сигнала размера
size со степенью перекрытия overlap.
"""


def get_frames(signal, size, overlap):
    step = int(size * overlap)
    start = 0
    while start < len(signal) - 1:
        yield signal[start: start + size]
        start += step


signal = [1, 2, 3, 4, 5, 6, 7, 8]
for el in get_frames(signal,4,0.5):
	print(el)