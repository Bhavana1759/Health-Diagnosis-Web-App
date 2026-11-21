import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.border.EmptyBorder;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.net.URL;
import java.util.*;
import java.util.List;

public class App extends JFrame {

    private static final String BG_URL = "https://pwc.com";
    private BufferedImage backgroundImage;

    private final JComboBox<String> diseaseSelector;
    private final JLabel titleLabel;
    private final JPanel leftColumn;
    private final JPanel rightColumn;
    private final JButton predictButton;
    private final JLabel resultLabel;
    private final List<JTextField> inputFields = new ArrayList<>();

    private static class DiseaseConfig {
        String title;
        String buttonText;
        String[] leftLabels;
        String[] rightLabels;

        DiseaseConfig(String title, String buttonText, String[] leftLabels, String[] rightLabels) {
            this.title = title;
            this.buttonText = buttonText;
            this.leftLabels = leftLabels;
            this.rightLabels = rightLabels;
        }
    }

    private final Map<String, DiseaseConfig> configs = new LinkedHashMap<>();

    public App() {
        setTitle("Disease Prediction");
        setSize(1050, 750);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        loadBackgroundImage();
        initConfigs();

        // Main Background Panel with Dark Overlay
        JPanel mainPanel = new JPanel(new BorderLayout(0, 20)) {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                if (backgroundImage != null) {
                    g.drawImage(backgroundImage, 0, 0, getWidth(), getHeight(), this);
                } else {
                    g.setColor(new Color(20, 30, 48));
                    g.fillRect(0, 0, getWidth(), getHeight());
                }
                g.setColor(new Color(0, 0, 0, 140)); // rgba(0,0,0,0.55) overlay
                g.fillRect(0, 0, getWidth(), getHeight());
            }
        };
        mainPanel.setBorder(new EmptyBorder(30, 60, 30, 60));

        // Top Section: Selector + Title
        JPanel topPanel = new JPanel();
        topPanel.setLayout(new BoxLayout(topPanel, BoxLayout.Y_AXIS));
        topPanel.setOpaque(false);

        JLabel selectLabel = new JLabel("Select Disease");
        selectLabel.setForeground(Color.WHITE);
        selectLabel.setFont(new Font("SansSerif", Font.BOLD, 14));
        selectLabel.setAlignmentX(Component.LEFT_ALIGNMENT);

        diseaseSelector = new JComboBox<>(configs.keySet().toArray(new String[0]));
        diseaseSelector.setMaximumSize(new Dimension(Integer.MAX_VALUE, 38));
        diseaseSelector.setFont(new Font("SansSerif", Font.PLAIN, 15));
        diseaseSelector.setAlignmentX(Component.LEFT_ALIGNMENT);

        titleLabel = new JLabel("Diabetes Prediction");
        titleLabel.setForeground(Color.WHITE);
        titleLabel.setFont(new Font("SansSerif", Font.BOLD, 30));
        titleLabel.setBorder(new EmptyBorder(20, 0, 10, 0));
        titleLabel.setAlignmentX(Component.LEFT_ALIGNMENT);

        topPanel.add(selectLabel);
        topPanel.add(Box.createVerticalStrut(6));
        topPanel.add(diseaseSelector);
        topPanel.add(titleLabel);

        // Center Section: Two-Column Form inside Transparent ScrollPane
        JPanel columnsPanel = new JPanel(new GridLayout(1, 2, 40, 0));
        columnsPanel.setOpaque(false);

        leftColumn = new JPanel();
        leftColumn.setLayout(new BoxLayout(leftColumn, BoxLayout.Y_AXIS));
        leftColumn.setOpaque(false);

        rightColumn = new JPanel();
        rightColumn.setLayout(new BoxLayout(rightColumn, BoxLayout.Y_AXIS));
        rightColumn.setOpaque(false);

        columnsPanel.add(leftColumn);
        columnsPanel.add(rightColumn);

        JScrollPane scrollPane = new JScrollPane(columnsPanel);
        scrollPane.setOpaque(false);
        scrollPane.getViewport().setOpaque(false);
        scrollPane.setBorder(null);
        scrollPane.getVerticalScrollBar().setUnitIncrement(16);

        // Bottom Section: Predict Button + Result Banner
        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new BoxLayout(bottomPanel, BoxLayout.Y_AXIS));
        bottomPanel.setOpaque(false);

        predictButton = new JButton("Predict Diabetes");
        predictButton.setFont(new Font("SansSerif", Font.BOLD, 15));
        predictButton.setBackground(new Color(0, 168, 107));
        predictButton.setForeground(Color.WHITE);
        predictButton.setFocusPainted(false);
        predictButton.setBorder(new EmptyBorder(10, 24, 10, 24));
        predictButton.setCursor(new Cursor(Cursor.HAND_CURSOR));
        predictButton.setAlignmentX(Component.LEFT_ALIGNMENT);

        resultLabel = new JLabel(" ");
        resultLabel.setOpaque(true);
        resultLabel.setBackground(new Color(0, 168, 107, 220));
        resultLabel.setForeground(Color.WHITE);
        resultLabel.setFont(new Font("SansSerif", Font.BOLD, 16));
        resultLabel.setBorder(new EmptyBorder(12, 16, 12, 16));
        resultLabel.setMaximumSize(new Dimension(Integer.MAX_VALUE, 48));
        resultLabel.setAlignmentX(Component.LEFT_ALIGNMENT);
        resultLabel.setVisible(false);

        bottomPanel.add(predictButton);
        bottomPanel.add(Box.createVerticalStrut(15));
        bottomPanel.add(resultLabel);

        mainPanel.add(topPanel, BorderLayout.NORTH);
        mainPanel.add(scrollPane, BorderLayout.CENTER);
        mainPanel.add(bottomPanel, BorderLayout.SOUTH);

        setContentPane(mainPanel);

        // Event Listeners
        diseaseSelector.addActionListener(e -> renderForm());
        predictButton.addActionListener(e -> runPrediction());

        renderForm();
    }

    private void loadBackgroundImage() {
        try {
            backgroundImage = ImageIO.read(new URL(BG_URL));
        } catch (Exception ignored) {
            // Falls back to dark navy gradient if offline
        }
    }

    private void initConfigs() {
        configs.put("Diabetes Prediction", new DiseaseConfig(
                "Diabetes Prediction",
                "Predict Diabetes",
                new String[]{
                        "Pregnancies (No. of times pregnant)",
                        "Glucose Level (80–130 mg/dL)",
                        "Blood Pressure (Normal <130/80)",
                        "Skin Thickness (10–30 mm)"
                },
                new String[]{
                        "Insulin Level (10–25 µU/mL)",
                        "BMI (18.5–24.9 kg/m²)",
                        "Diabetes Pedigree Function (0.1–2.5)",
                        "Age (Years)"
                }
        ));

        configs.put("Heart Disease Prediction", new DiseaseConfig(
                "Heart Disease Prediction",
                "Predict Heart Disease",
                new String[]{
                        "Age (Years)",
                        "Sex (1 = Male, 0 = Female)",
                        "Chest Pain Type (0–3)",
                        "Resting BP (Ideal <120/80)",
                        "Cholesterol (Total <200 mg/dL)",
                        "Fasting Blood Sugar (>120 = 1)",
                        "Thal (0=Normal,1=Fixed,2=Reversible)"
                },
                new String[]{
                        "Rest ECG (0–2)",
                        "Max Heart Rate (90–190 BPM)",
                        "Exercise Angina (1=Yes,0=No)",
                        "Oldpeak (0–2 mm)",
                        "Slope (0–2)",
                        "Major Vessels (0–3)"
                }
        ));

        configs.put("Parkinsons Prediction", new DiseaseConfig(
                "Parkinson's Disease Prediction",
                "Predict Parkinson's",
                new String[]{
                        "Fo (85–165 Hz)", "Fhi (165–350 Hz)", "Flo (60–165 Hz)",
                        "Jitter % (0.2–3.5%)", "Jitter Abs (0.01–0.1)", "RAP (0.5–2.5%)",
                        "PPQ (0.5–2.5%)", "DDP (0.6–7.5%)", "Shimmer (1–7%)",
                        "Shimmer dB (0.1–1.5)", "APQ3 (0.5–5%)"
                },
                new String[]{
                        "APQ5 (1–6%)", "APQ (1.5–7%)", "DDA (1–9%)", "NHR (0.11–0.35)",
                        "HNR (10–25 dB)", "RPDE (0.3–0.6)", "DFA (0.5–1.0)",
                        "Spread1 (0.8–1.7)", "Spread2 (0–4)", "D2 (Dopamine Receptor)", "PPE (0.1–0.3)"
                }
        ));

        configs.put("Lung Cancer Prediction", new DiseaseConfig(
                "Lung Cancer Prediction",
                "Predict Lung Cancer",
                new String[]{
                        "Gender (1=Male,0=Female)", "Age (Years)", "Smoking (1=Yes,0=No)",
                        "Yellow Fingers (1=Yes,0=No)", "Anxiety (1=Yes,0=No)",
                        "Peer Pressure (1=Yes,0=No)", "Chronic Disease (1=Yes,0=No)", "Fatigue (1=Yes,0=No)"
                },
                new String[]{
                        "Allergy (1=Yes,0=No)", "Wheezing (1=Yes,0=No)", "Alcohol (1=Yes,0=No)",
                        "Coughing (1=Yes,0=No)", "Shortness of Breath (1=Yes,0=No)",
                        "Swallowing Difficulty (1=Yes,0=No)", "Chest Pain (1=Yes,0=No)"
                }
        ));

        configs.put("Hypo-Thyroid Prediction", new DiseaseConfig(
                "Hypo-Thyroid Prediction",
                "Predict Thyroid",
                new String[]{
                        "Age (Years)", "Sex (1=Male,0=Female)", "On Thyroxine (1=Yes,0=No)"
                },
                new String[]{
                        "TSH (0.4–4.0 mIU/L)", "T3 (80–200 ng/dL)", "T4 (5–12 µg/dL)"
                }
        ));
    }

