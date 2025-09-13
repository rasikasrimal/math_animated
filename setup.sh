#!/bin/bash
# Setup script for Math Animated project

echo "🚀 Math Animated - Setup Script"
echo "================================"

# Function to detect OS
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if [ -f /etc/debian_version ]; then
            echo "debian"
        elif [ -f /etc/redhat-release ]; then
            echo "redhat"
        else
            echo "linux"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "macos"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        echo "windows"
    else
        echo "unknown"
    fi
}

# Function to install system dependencies
install_system_deps() {
    OS=$(detect_os)
    echo "Detected OS: $OS"
    
    case $OS in
        "debian")
            echo "📦 Installing system dependencies for Debian/Ubuntu..."
            sudo apt-get update
            sudo apt-get install -y build-essential python3-dev python3-pip \
                libcairo2-dev libpango1.0-dev pkg-config
            ;;
        "redhat")
            echo "📦 Installing system dependencies for RedHat/CentOS..."
            sudo yum groupinstall -y "Development Tools"
            sudo yum install -y python3-devel python3-pip cairo-devel pango-devel pkgconfig
            ;;
        "macos")
            echo "📦 Installing system dependencies for macOS..."
            if ! command -v brew &> /dev/null; then
                echo "❌ Homebrew not found. Please install Homebrew first:"
                echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
                exit 1
            fi
            brew install cairo pango glib pkg-config
            ;;
        "windows")
            echo "🪟 For Windows, please use WSL (Windows Subsystem for Linux) or install:"
            echo "   - Visual Studio Build Tools"
            echo "   - Cairo and Pango libraries"
            echo "   See: https://docs.manim.community/en/stable/installation/windows.html"
            ;;
        *)
            echo "❓ Unknown OS. Please install the following manually:"
            echo "   - Build tools (gcc, make, etc.)"
            echo "   - Python development headers"
            echo "   - Cairo development libraries"
            echo "   - Pango development libraries"
            echo "   - pkg-config"
            ;;
    esac
}

# Function to install Python dependencies
install_python_deps() {
    echo ""
    echo "🐍 Installing Python dependencies..."
    
    # Check if virtual environment should be used
    read -p "Do you want to create a virtual environment? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
        source venv/bin/activate
        echo "✅ Virtual environment created and activated"
    fi
    
    # Install requirements
    if [ -f "requirements.txt" ]; then
        pip install -r requirements.txt
        echo "✅ Python dependencies installed"
    else
        echo "❌ requirements.txt not found"
        exit 1
    fi
}

# Function to test installation
test_installation() {
    echo ""
    echo "🧪 Testing installation..."
    
    if python test_project.py; then
        echo ""
        echo "🎉 Setup completed successfully!"
        echo ""
        echo "📚 Quick start:"
        echo "   python main.py list       # List all animations"
        echo "   python main.py quadratic  # Run quadratic function animation"
        echo "   python main.py all        # Run all animations"
        echo ""
        echo "🎬 Your animations will be saved in the 'media' directory"
    else
        echo "❌ Setup test failed. Please check the output above."
        exit 1
    fi
}

# Main execution
main() {
    echo "This script will install system dependencies and Python packages for Manim."
    echo "You may be prompted for your password to install system packages."
    echo ""
    
    read -p "Continue with setup? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Setup cancelled."
        exit 0
    fi
    
    install_system_deps
    install_python_deps
    test_installation
}

# Run main function
main