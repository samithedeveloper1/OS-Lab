def fifo_page_replacement(pages, frame_capacity):
    frame = []
    hit_count = 0
    miss_count = 0

    print("Page\tFrame\t\tStatus")
    for page in pages:
        if page in frame:
            hit_count += 1
            status = "Hit"
        else:
            miss_count += 1
            if len(frame) >= frame_capacity:
                frame.pop(0)  
            frame.append(page)
            status = "Miss"
        
        print(f"{page}\t{frame}\t{status}")
    
    return hit_count, miss_count



pages = [0, 1, 5, 3, 5, 0, 2, 4, 7, 9, 0, 0, 3]
frame_size = 4


hits, misses = fifo_page_replacement(pages, frame_size)

print("\nTotal Hits:", hits)
print("Total Misses:", misses)
