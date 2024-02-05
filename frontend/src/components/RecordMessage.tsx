import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";

type Props = {
  handleStart: any;
};
function RecordMessage({ handleStart }: Props) {
  return (
    <ReactMediaRecorder
      audio
      onStart={handleStart}
      // onStop={handleStop}
      render={({ status, startRecording, stopRecording }) => (
        <div className="mt-2">
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className="bg-white p-4 rounded-full"
          >
            <RecordIcon
              classText={
                status == "recording"
                  ? "animate-pulse text-red-500"
                  : "animate-pulse text-sky-500"
              }
            />
          </button>
          <p className="mt-2 text-white font-light">{status}</p>
        </div>
      )}
    />
  );
}

export default RecordMessage;
