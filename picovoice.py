import pvporcupine
import pyaudio
import struct


def picovoice_run():
    """
     Creates an input audio stream, instantiates an instance of Porcupine object, and monitors the audio stream for
     occurrences of the wake word(s). It prints the time of detection for each occurrence and the wake word.
     """
    # keywords = list()
    # for x in self._keyword_paths:
    #     keywords.append(os.path.basename(x).replace('.ppn', '').split('_')[0])

    porcupine = None
    pa = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(keywords=['picovoice', 'bumblebee', 'jarvis'])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length,
            input_device_index=None)

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
            result = porcupine.process(pcm)
            if result >= 0:
                break

    except KeyboardInterrupt:
        print('Stopping ...')
    finally:
        print("Stop")
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()

# picovoice_run()
