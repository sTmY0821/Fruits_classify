from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

dataset = ImageFolder('data', transform=transform)
loader = DataLoader(dataset, batch_size=4, shuffle=True)