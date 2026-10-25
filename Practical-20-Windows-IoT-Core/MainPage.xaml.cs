using Windows.UI.Xaml.Controls;

namespace HelloIoT
{
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            InitializeComponent();
            var message = new TextBlock
            {
                Text = "Hello Windows IoT Core!",
                FontSize = 40
            };
            Content = message;
        }
    }
}
