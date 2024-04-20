import React, { useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { Typography, CircularProgress } from "@mui/material";
import axios from "axios";

const FileUpload = ({ onFileUpload, loading }) => {
  const onDrop = useCallback(
    async (acceptedFiles) => {
      // Do something with the uploaded file(s)
      if (acceptedFiles && acceptedFiles.length > 0) {
        try {
          const formData = new FormData();
          acceptedFiles.forEach((file) => {
            formData.append("files[]", file);
          });

          // Make a POST request to the backend with the uploaded files
          const response = await axios.post(
            "http://localhost:8080/upload", // Change the URL to your backend endpoint
            formData,
            {
              headers: {
                "Content-Type": "multipart/form-data",
              },
            }
          );

          // Call the callback function with the response data
          onFileUpload(response.data);
        } catch (error) {
          console.error("Error uploading file:", error);
        }
      }
    },
    [onFileUpload]
  );

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()} style={dropzoneStyle}>
      <input {...getInputProps()} />
      {isDragActive ? (
        <Typography variant="body1">Drop the files here...</Typography>
      ) : (
        <Typography variant="body1">
          Drag 'n' drop some files here, or click to select files
        </Typography>
      )}
      {loading && <CircularProgress color="secondary" />}
    </div>
  );
};

const dropzoneStyle = {
  border: "2px dashed #ccc",
  borderRadius: "4px",
  padding: "20px",
  textAlign: "center",
  cursor: "pointer",
};

export default FileUpload;
