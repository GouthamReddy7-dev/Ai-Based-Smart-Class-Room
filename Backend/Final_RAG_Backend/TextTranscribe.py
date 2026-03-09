from faster_whisper import WhisperModel

def TranscribeText(path):
    model_size="small"
    model=WhisperModel(model_size,device="cpu",compute_type="int8")
    segement,info=model.transcribe(path)
    data=""
    for seg in segement:
        print(seg.text)
        data+=seg.text
    return data    
    