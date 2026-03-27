import gradio as gr
import numpy as np
import joblib

# Load trained model and scaler
model_cla = joblib.load("Model/best_model_SVM.pkl")

# Label mapping
label_map = {3: "Best (obsolescence_time >= 8)", 2: "Good (6 <= Obsolescence_time < 8)", 1: "Below Average (4 <= obsolescence_time < 6)", 0: "Worst (obsolescence_time < 4)"}

# Prediction function
def predict(Processor_Speed_GHz, RAM_GB, Storage_GB, Battery_mAh, Display_Tech, Connectivity,
            Camera_Score, Update_Support_Years, Security_Updates_Per_Year, Brand_Score,
            Release_Year, Initial_Price_USD, Customer_Rating):

    try:

        input_data = np.array([[Processor_Speed_GHz, RAM_GB, Storage_GB, Battery_mAh,
                                Display_Tech, Connectivity, Camera_Score,
                                Update_Support_Years, Security_Updates_Per_Year,
                                Brand_Score, Release_Year, Initial_Price_USD,
                                Customer_Rating]])

        prediction = model_cla.predict(input_data)[0]

        return label_map.get(prediction, "Unknown")

    except Exception as e:
        return str(e)


# Gradio UI
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Processor Speed (GHz)"),
        gr.Number(label="RAM (GB)"),
        gr.Number(label="Storage (GB)"),
        gr.Number(label="Battery (mAh)"),
        gr.Number(label="Display Tech"),
        gr.Number(label="Connectivity"),
        gr.Number(label="Camera Score"),
        gr.Number(label="Update Support Years"),
        gr.Number(label="Security Updates Per Year"),
        gr.Number(label="Brand Score"),
        gr.Number(label="Release Year"),
        gr.Number(label="Initial Price USD"),
        gr.Number(label="Customer Rating")
    ],
    outputs="text",
    title="Smartphone Obsolescence Predictor",
    description="Enter smartphone specifications to predict obsolescence category"
)

demo.launch()
