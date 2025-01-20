import mido
from mido import MidiFile

def get_midi_length(file_path):
    try:
        midi = MidiFile(file_path)
        total_time = 0
        ticks_per_beat = midi.ticks_per_beat
        tempo = 500000  # Default tempo in microseconds per beat (120 bpm)

        for i, track in enumerate(midi.tracks):
            track_time = 0
            for msg in track:
                try:
                    if not msg.is_meta and hasattr(msg, 'time'):
                        # Custom data handling, allowing bytes to go above 127
                        track_time += msg.time
                except Exception as inner_e:
                    print(f"Error processing message in track {i}: {inner_e}")
                    continue
                
                # Check for tempo change messages
                if msg.type == 'set_tempo':
                    tempo = msg.tempo

            total_time = max(total_time, track_time)

        # Convert total time from ticks to seconds
        seconds_per_beat = tempo / 1000000.0
        seconds_per_tick = seconds_per_beat / ticks_per_beat
        total_seconds = total_time * seconds_per_tick

        # Convert total_seconds to appropriate time units
        total_minutes = total_seconds / 60
        total_hours = total_minutes / 60
        total_days = total_hours / 24
        total_years = total_days / 365.25  # Considering leap years

        return {
            'seconds': total_seconds,
            'minutes': total_minutes,
            'hours': total_hours,
            'days': total_days,
            'years': total_years
        }
    except Exception as e:
        print(f"Error reading MIDI file: {e}")
        return None

# Example usage
file_path = 'supposedly the longest midi.mid'  # Replace with your MIDI file path
length = get_midi_length(file_path)
if length:
    print(f"MIDI Length: {length['seconds']} seconds ({length['minutes']} minutes, {length['hours']} hours, {length['days']} days, {length['years']} years)")
