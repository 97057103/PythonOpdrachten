import os
from PIL import Image

def resize_image(image_path, output_path, max_size):
    with Image.open(image_path) as img:
        img.thumbnail((max_size, max_size))
        img.save(output_path)
        print(f"Aangepast: {os.path.basename(image_path)}")

def is_image_file(filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def main():
    source = input("Pad naar de bronmap met afbeeldingen: ").strip()
    destination = input("Pad naar de uitvoermap: ").strip()
    max_size = int(input("Maximale afmeting van afbeeldingen (max 2000): ").strip())

    if max_size > 2000:
        print("Maximale toegestane afmeting is 2000 pixels.")
        return

    if not os.path.isdir(source):
        print("De opgegeven bronmap bestaat niet.")
        return

    if not os.path.exists(destination):
        os.makedirs(destination)

    files = os.listdir(source)
    image_files = [f for f in files if is_image_file(f)]

    print(f"\nGevonden {len(image_files)} afbeeldingsbestanden in '{source}'.")

    for filename in files:
        source_path = os.path.join(source, filename)

        if not is_image_file(filename):
            print(f"Overgeslagen (geen afbeelding): {filename}")
            continue

        output_path = os.path.join(destination, filename)
        try:
            resize_image(source_path, output_path, max_size)
        except Exception as e:
            print(f"Fout bij verwerken van {filename}: {e}")

    print("\nAlle afbeeldingen zijn aangepast en opgeslagen.")

if __name__ == "__main__":
    main()
