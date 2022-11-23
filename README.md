# AI Video transcriptor

Python program we are going to transcribe a Youtube video to text with the help of AI.

## Installation

Is needed the installation of pytube, whisper and ffmpeg.

```bash
pip install pytube
pip install whisper
pip install ffmpeg-python
```

## Usage

```python
#From an input Youtube Link the trasncriber will be processed.
input("Please enter the Youtube Link of the video you want to transcribe: ")

#Also it will ask you if you want to save the result in a .txt.
input('Do you want to print the result in a .txt? (y/n): ').lower().strip() == 'y'

#Ask if want to delete the temporal downloaded video
input('Do you want to delete the temporal downloaded video? (y/n): ').lower().strip() == 'y'

```

## Contributing

Pull requests are welcome. Please open an issue first to discuss what you would like to change.

## License

[VICTOR DORADO](https://github.com/vdfbiz7/)
