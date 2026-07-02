import os


class FileWriter:

    def __init__(self, data):

        self.data = data

    def save_excel(self):

        os.makedirs("outputs", exist_ok=True)

        output_file = "outputs/Processed_RC1_Data.xlsx"

        self.data.to_excel(
            output_file,
            index=False
        )

        print(f"\nFile saved successfully!")

        print(output_file)
        