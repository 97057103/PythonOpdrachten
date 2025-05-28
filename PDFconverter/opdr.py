import os
from pathlib import Path
from fpdf import FPDF
from PIL import Image

def get_existing_folder(prompt):
    while True:
        folder = input(prompt)
        if os.path.isdir(folder):
            return folder
        print("❌ Map bestaat niet. Probeer opnieuw.")

def get_output_filename(output_folder):
    while True:
        filename = input("Geef de naam van het uitvoerbestand (bijv. output.pdf): ")
        if not filename.endswith(".pdf"):
            print("❌ Bestandsnaam moet eindigen op .pdf")
            continue
        output_path = os.path.join(output_folder, filename)
        if os.path.exists(output_path):
            print("❌ Bestand bestaat al in deze map. Kies een andere naam.")
            continue
        return output_path

def convert_images_to_pdf(source_folder, output_path):
    pdf = FPDF(unit="pt")  # Gebruik punten voor nauwkeurige maatvoering
    jpg_count = 0

    for file in sorted(os.listdir(source_folder)):
        if file.lower().endswith(".jpg"):
            image_path = os.path.join(source_folder, file)
            img = Image.open(image_path)
            width, height = img.size

            pdf.add_page(format=(width, height))
            pdf.image(image_path, x=0, y=0, w=width, h=height)
            jpg_count += 1
        else:
            print(f"⏭ Bestand overgeslagen (geen .jpg): {file}")

    if jpg_count == 0:
        print("⚠️ Geen .jpg-bestanden gevonden. PDF niet aangemaakt.")
    else:
        pdf.output(output_path)
        print(f"✅ PDF opgeslagen als: {output_path}")

def main():
    print("=== JPG naar PDF Converter ===")
    source_folder = get_existing_folder("📁 Geef het pad naar de map met afbeeldingen: ")
    output_folder = get_existing_folder("💾 Geef het pad waar het PDF-bestand moet worden opgeslagen: ")
    output_path = get_output_filename(output_folder)
    convert_images_to_pdf(source_folder, output_path)

if __name__ == "__main__":
    main()
